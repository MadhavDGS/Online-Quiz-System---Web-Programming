from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from quiz_data import QUIZ_DATA

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

def initialize_session():
    if 'current_unit' not in session:
        session['current_unit'] = 'UNIT-1'
    if 'user_answers' not in session:
        session['user_answers'] = {}
    if 'current_page' not in session:
        session['current_page'] = 0
    if 'submitted' not in session:
        session['submitted'] = False

def calculate_score():
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

@app.route('/')
def index():
    initialize_session()
    current_unit = session.get('current_unit', 'UNIT-1')
    current_page = session.get('current_page', 0)
    page_size = 1  # Changed from 10 to 1 to show one question per page
    
    questions = QUIZ_DATA[current_unit]
    total_pages = len(questions)  # Each question gets its own page
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

@app.route('/select_unit', methods=['POST'])
def select_unit():
    unit = request.form.get('unit')
    if unit in QUIZ_DATA:
        session['current_unit'] = unit
        session['current_page'] = 0
    return redirect(url_for('index'))

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    question_key = request.form.get('question_key')
    answer = request.form.get('answer')
    if 'user_answers' not in session:
        session['user_answers'] = {}
    user_answers = dict(session['user_answers'])
    user_answers[question_key] = answer
    session['user_answers'] = user_answers
    
    # Handle next page navigation if next=true in form data
    if request.form.get('next') == 'true':
        current_page = session.get('current_page', 0)
        current_unit = session.get('current_unit', 'UNIT-1')
        total_pages = len(QUIZ_DATA[current_unit])
        if current_page < total_pages - 1:
            session['current_page'] = current_page + 1
    
    return redirect(url_for('index'))

@app.route('/navigate', methods=['POST'])
def navigate():
    action = request.form.get('action')
    current_page = session.get('current_page', 0)
    current_unit = session.get('current_unit', 'UNIT-1')
    total_pages = len(QUIZ_DATA[current_unit])  # Each question gets its own page
    
    if action == 'previous' and current_page > 0:
        session['current_page'] = current_page - 1
    elif action == 'next' and current_page < total_pages - 1:
        session['current_page'] = current_page + 1
        
    return redirect(url_for('index'))

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    session['submitted'] = True
    return redirect(url_for('index'))

@app.route('/reset_quiz', methods=['POST'])
def reset_quiz():
    session.clear()
    return redirect(url_for('index'))

@app.route('/get_answered_questions', methods=['POST'])
def get_answered_questions():
    data = request.get_json()
    saved_answers = data.get('answers', {})
    answered_questions = []
    
    for key, answer in saved_answers.items():
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
    
    return jsonify(answered_questions)

if __name__ == '__main__':
    app.run(debug=True) 