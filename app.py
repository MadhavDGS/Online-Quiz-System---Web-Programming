from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from quiz_data import QUIZ_DATA
import logging

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_default_unit():
    """Returns the first available unit from QUIZ_DATA or UNIT-3 if it exists"""
    if 'UNIT-3' in QUIZ_DATA:
        return 'UNIT-3'
    return list(QUIZ_DATA.keys())[0] if QUIZ_DATA else 'UNIT-3'

def initialize_session():
    """Initialize or repair session data"""
    try:
        default_unit = get_default_unit()
        
        # Initialize or repair current_unit
        if 'current_unit' not in session or session['current_unit'] not in QUIZ_DATA:
            session['current_unit'] = default_unit
        
        # Initialize or repair other session variables
        if 'user_answers' not in session:
            session['user_answers'] = {}
        if 'current_page' not in session:
            session['current_page'] = 0
        if 'submitted' not in session:
            session['submitted'] = False
            
        # Validate current_page
        current_unit = session['current_unit']
        total_pages = len(QUIZ_DATA[current_unit])
        if session['current_page'] >= total_pages:
            session['current_page'] = 0
            
    except Exception as e:
        logger.error(f"Error in initialize_session: {str(e)}")
        # Reset to safe defaults
        session['current_unit'] = default_unit
        session['current_page'] = 0
        session['user_answers'] = {}
        session['submitted'] = False

def calculate_score():
    try:
        total_questions = 0
        correct_answers = 0
        unit_scores = {}
        
        for unit in QUIZ_DATA:
            unit_correct = 0
            unit_total = len(QUIZ_DATA[unit])
            total_questions += unit_total
            
            for i, question in enumerate(QUIZ_DATA[unit]):
                question_key = f"{unit}_{i}"
                if question_key in session.get('user_answers', {}):
                    if session['user_answers'][question_key] == question['correct_answer']:
                        correct_answers += 1
                        unit_correct += 1
            
            unit_scores[unit] = {
                'correct': unit_correct,
                'total': unit_total,
                'percentage': (unit_correct / unit_total * 100) if unit_total > 0 else 0
            }
        
        total_percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        return {
            'total_correct': correct_answers,
            'total_questions': total_questions,
            'total_percentage': total_percentage,
            'unit_scores': unit_scores
        }
    except Exception as e:
        logger.error(f"Error in calculate_score: {str(e)}")
        return {
            'total_correct': 0,
            'total_questions': 0,
            'total_percentage': 0,
            'unit_scores': {}
        }

@app.route('/')
def index():
    try:
        # Initialize or repair session
        initialize_session()
        
        # Get current unit (will always be valid due to initialize_session)
        current_unit = session['current_unit']
        current_page = session['current_page']
        
        # Get questions for current unit
        questions = QUIZ_DATA[current_unit]
        total_pages = len(questions)
        
        # Calculate page range
        page_size = 1
        start_idx = current_page * page_size
        end_idx = min(start_idx + page_size, len(questions))
        current_questions = questions[start_idx:end_idx]
        
        return render_template('index.html',
                             units=list(QUIZ_DATA.keys()),
                             current_unit=current_unit,
                             current_page=current_page,
                             total_pages=total_pages,
                             questions=current_questions,
                             start_idx=start_idx,
                             user_answers=session.get('user_answers', {}),
                             submitted=session.get('submitted', False),
                             scores=calculate_score() if session.get('submitted', False) else None,
                             quiz_data=QUIZ_DATA)
    except Exception as e:
        logger.error(f"Error in index route: {str(e)}")
        session.clear()
        initialize_session()  # Reinitialize with safe defaults
        return redirect(url_for('index'))

@app.route('/select_unit', methods=['POST'])
def select_unit():
    try:
        unit = request.form.get('unit')
        if unit in QUIZ_DATA:
            session['current_unit'] = unit
            session['current_page'] = 0
        return redirect(url_for('index'))
    except Exception as e:
        logger.error(f"Error in select_unit: {str(e)}")
        return redirect(url_for('index'))

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    try:
        question_key = request.form.get('question_key')
        answer = request.form.get('answer')
        if not question_key or not answer:
            return redirect(url_for('index'))
            
        if 'user_answers' not in session:
            session['user_answers'] = {}
        user_answers = dict(session['user_answers'])
        user_answers[question_key] = answer
        session['user_answers'] = user_answers
        
        if request.form.get('next') == 'true':
            current_page = session.get('current_page', 0)
            current_unit = session.get('current_unit', get_default_unit())
            if current_unit in QUIZ_DATA:
                total_pages = len(QUIZ_DATA[current_unit])
                if current_page < total_pages - 1:
                    session['current_page'] = current_page + 1
        
        return redirect(url_for('index'))
    except Exception as e:
        logger.error(f"Error in submit_answer: {str(e)}")
        return redirect(url_for('index'))

@app.route('/navigate', methods=['POST'])
def navigate():
    try:
        action = request.form.get('action')
        current_page = session.get('current_page', 0)
        current_unit = session.get('current_unit', get_default_unit())
        
        if current_unit in QUIZ_DATA:
            total_pages = len(QUIZ_DATA[current_unit])
            if action == 'previous' and current_page > 0:
                session['current_page'] = current_page - 1
            elif action == 'next' and current_page < total_pages - 1:
                session['current_page'] = current_page + 1
        
        return redirect(url_for('index'))
    except Exception as e:
        logger.error(f"Error in navigate: {str(e)}")
        return redirect(url_for('index'))

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    try:
        session['submitted'] = True
        return redirect(url_for('index'))
    except Exception as e:
        logger.error(f"Error in submit_quiz: {str(e)}")
        return redirect(url_for('index'))

@app.route('/reset_quiz', methods=['POST'])
def reset_quiz():
    try:
        session.clear()
        initialize_session()  # Reinitialize with safe defaults
        return redirect(url_for('index'))
    except Exception as e:
        logger.error(f"Error in reset_quiz: {str(e)}")
        return redirect(url_for('index'))

@app.route('/get_answered_questions', methods=['POST'])
def get_answered_questions():
    try:
        data = request.get_json()
        if not data:
            return jsonify([])
            
        saved_answers = data.get('answers', {})
        answered_questions = []
        
        for key, answer in saved_answers.items():
            try:
                unit, index = key.split('_')
                index = int(index)
                if unit in QUIZ_DATA and index < len(QUIZ_DATA[unit]):
                    question_data = QUIZ_DATA[unit][index]
                    answered_questions.append({
                        'unit': unit,
                        'index': index,
                        'question': question_data['question'],
                        'answer': answer
                    })
            except (ValueError, KeyError):
                continue
        
        return jsonify(answered_questions)
    except Exception as e:
        logger.error(f"Error in get_answered_questions: {str(e)}")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True) 