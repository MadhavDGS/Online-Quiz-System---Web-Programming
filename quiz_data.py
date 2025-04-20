# Predefined questions and answers
QUIZ_DATA = {
    "UNIT-3": [
        {
            "question": "When does Exceptions in Java arises in code sequence?",
            "options": ["Run Time", "Compilation Time", "Can Occur Any Time", "None of the mentioned"],
            "correct_answer": "Compilation Time"
        },
        {
            "question": "Which of these keywords is not a part of exception handling?",
            "options": ["try", "finally", "thrown", "catch"],
            "correct_answer": "thrown"
        },
        {
            "question": "Which of these keywords must be used to monitor for exceptions?",
            "options": ["try", "finally", "throw", "catch"],
            "correct_answer": "try"
        },
        {
            "question": "Which of these keywords must be used to handle the exception thrown by try block in some rational manner?",
            "options": ["try", "finally", "throw", "catch"],
            "correct_answer": "catch"
        },
        {
            "question": "Which of these keywords is used to manually throw an exception?",
            "options": ["try", "finally", "throw", "catch"],
            "correct_answer": "throw"
        },
        {
            "question": "In Java, exceptions are divided into two categories, namely checked and unchecked exceptions.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "The subclass exception should precede the base class exception when used within the catch clause.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "What are checked exceptions?",
            "options": ["checked by java compiler", "checked by java virtual machine", "above two", "none of the above"],
            "correct_answer": "checked by java compiler"
        },
        {
            "question": "Is it possible to re-throw exceptions",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "What are unchecked exceptions?",
            "options": ["checked by java compiler", "checked by java virtual machine", "above two", "none of the above"],
            "correct_answer": "checked by java virtual machine"
        },
        {
            "question": "exception is available in util package",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "The statements following the throw keyword in a program are not executed.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Finally block will get invoke whether the exception is thrown or not.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "If you throw an exception in your code, then you must declare it using the throws keyword in your method declaration.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Match each situation with the correct outcome: a)int[] A; A[0] = 0; b)JVM can't find Java platform classes c)End of stream marker d)Read after end of stream",
            "options": [
                "a-2,b-1,c-3,d-4",
                "a-4,b-3,b-2,c-1",
                "a-3,b-1,c-4,d-2",
                "a-1,b-2,c-3,d-4"
            ],
            "correct_answer": "a-3,b-1,c-4,d-2"
        },
        {
            "question": "Creating an exception object and handling it to the run time system is called __________.",
            "options": ["exception handler", "catch the exception", "pass the exception", "throwing an exception"],
            "correct_answer": "throwing an exception"
        },
        {
            "question": "Pick runtime exception?",
            "options": ["ClassCastException", "FileNotFoundException", "NullPointerException", "SecurityException"],
            "correct_answer": "ClassCastException"
        },
        {
            "question": "Checked exceptions include all subtypes of Exception, including classes that extend RuntimeException.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Exceptions can be caught or rethrown to a calling method.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Which one of the following statement is correct?",
            "options": [
                "The 'try' block should be followed by a 'catch' block",
                "The 'try' block should be followed by a 'finally' block",
                "The 'try' block should be followed by either a 'catch' block or a 'finally' block",
                "The 'try' block should be followed by at least two 'catch' blocks"
            ],
            "correct_answer": "The 'try' block should be followed by either a 'catch' block or a 'finally' block"
        }
    ],
    "UNIT-4": [
        {
            "question": "Which of these methods is a part of Abstract Window Toolkit (AWT)?",
            "options": ["display()", "print()", "drawString()", "transient()"],
            "correct_answer": "drawString()"
        },
        {
            "question": "What does AWT stands for?",
            "options": ["All Window Tools", "All Writing Tools", "Abstract Window Toolkit", "Abstract Writing Toolkit"],
            "correct_answer": "Abstract Window Toolkit"
        },
        {
            "question": "Which of these package is used for text formatting in Java programming language?",
            "options": ["java.text", "java.awt", "java.awt.text", "java.io"],
            "correct_answer": "java.text"
        },
        {
            "question": "Where are the following four methods commonly used?",
            "options": [
                "public void add(Component c)",
                "public void setSize(int width,int height)",
                "public void setLayout(LayoutManager m)",
                "public void setVisible(boolean)"
            ],
            "correct_answer": "public void add(Component c)"
        },
        {
            "question": "Which is the container that doesn't contain title bar and MenuBars but it can have other components like button, textfield etc?",
            "options": ["Window", "Frame", "Panel", "Container"],
            "correct_answer": "Panel"
        },
        {
            "question": "In Graphics class which method is used to draws a rectangle with the specified width and height?",
            "options": [
                "public void drawRect(int x, int y, int width, int height)",
                "public abstract void fillRect(int x, int y, int width, int height)",
                "public abstract void drawLine(int x1, int y1, int x2, int y2)",
                "public abstract void drawOval(int x, int y, int width, int height)"
            ],
            "correct_answer": "public void drawRect(int x, int y, int width, int height)"
        },
        {
            "question": "Name the class used to represent a GUI application window, which is optionally resizable and can have a title bar, an icon, and menus.",
            "options": ["Window", "Panel", "Dialog", "Frame"],
            "correct_answer": "Frame"
        },
        {
            "question": "Which is a component in AWT that can contain another component like buttons, text fields, labels, etc.?",
            "options": ["Window", "Container", "Panel", "Frame"],
            "correct_answer": "Container"
        },
        {
            "question": "What are the different types of controls in AWT?",
            "options": ["Labels", "Pushbuttons", "Checkboxes", "Choice lists"],
            "correct_answer": "Choice lists"
        },
        {
            "question": "Which class provides many methods for graphics programming?",
            "options": ["java.awt", "java.Graphics", "java.awt.Graphics", "None of the above"],
            "correct_answer": "java.awt.Graphics"
        },
        {
            "question": "Which of these methods are used to register a keyboard event listener?",
            "options": ["KeyListener()", "addListener()", "addKeyListener()", "eventKeyboardListener()"],
            "correct_answer": "addKeyListener()"
        },
        {
            "question": "What is a listener in context to event handling?",
            "options": [
                "A listener is a variable that is notified when an event occurs",
                "A listener is an object that is notified when an event occurs",
                "A listener is a method that is notified when an event occurs",
                "A listener is a class that is notified when an event occurs"
            ],
            "correct_answer": "A listener is an object that is notified when an event occurs"
        },
        {
            "question": "Event class is defined in which of these libraries?",
            "options": ["java.io", "java.lang", "java.net", "java.util"],
            "correct_answer": "java.util"
        },
        {
            "question": "Which of these methods can be used to determine the type of event?",
            "options": ["getID()", "getSource()", "getEvent()", "getEventObject()"],
            "correct_answer": "getID()"
        },
        {
            "question": "Which of these class is super class of all the events?",
            "options": ["EventObject", "EventClass", "ActionEvent", "ItemEvent"],
            "correct_answer": "EventObject"
        },
        {
            "question": "Which of these events will be notified if scroll bar is manipulated?",
            "options": ["ActionEvent", "ComponentEvent", "AdjustmentEvent", "WindowEvent"],
            "correct_answer": "AdjustmentEvent"
        },
        {
            "question": "How many types of controls does AWT support?",
            "options": ["7", "6", "5", "8"],
            "correct_answer": "7"
        },
        {
            "question": "Which package provides many event classes and Listener interfaces for event handling?",
            "options": ["java.awt", "java.awt.Graphics", "java.awt.event", "java.event.listener"],
            "correct_answer": "java.awt.event"
        },
        {
            "question": "____ are classes that act as a connection point between event listeners and event sources?",
            "options": ["Event adapters", "Events Handler", "Event listener", "Jevent"],
            "correct_answer": "Event adapters"
        },
        {
            "question": "How many types of events are there?",
            "options": ["5", "3", "2", "4"],
            "correct_answer": "4"
        }
    ],
    "UNIT-5": [
        {
            "question": "Which of the following architecture does the Swing framework use?",
            "options": ["MVC", "MVP", "Layered architecture", "Master-Slave architecture"],
            "correct_answer": "MVC"
        },
        {
            "question": "Which of these functions is called to display the output of an applet?",
            "options": ["display()", "print()", "displayApplet()", "PrintApplet()"],
            "correct_answer": "print()"
        },
        {
            "question": "Which of these methods can be used to output a sting in an applet?",
            "options": ["display()", "print()", "drawString()", "transient()"],
            "correct_answer": "drawString()"
        },
        {
            "question": "A _____________ is a one-line input field that allows the user to choose a number or an object value from an ordered sequence?",
            "options": ["JTextarea", "Jtextfield", "Jspinner", "Jslider"],
            "correct_answer": "Jspinner"
        },
        {
            "question": "What is the most number of states a CheckBox can have?",
            "options": ["0", "1", "2", "3"],
            "correct_answer": "2"
        },
        {
            "question": "What is the standard prefix for the name of a CheckBox?",
            "options": ["chb", "chk", "ckb", "ckx"],
            "correct_answer": "chk"
        },
        {
            "question": "A CheckBox can also appear as a(n):",
            "options": ["button", "RadioButton", "ScrollBar", "Both a and b"],
            "correct_answer": "Both a and b"
        },
        {
            "question": "What is the standard prefix for the name of a RadioButton?",
            "options": ["rad", "rab", "rdo", "rdb"],
            "correct_answer": "rad"
        },
        {
            "question": "How many RadioButtons in a Group Box can be selected at the same time?",
            "options": ["0", "1", "2", "3"],
            "correct_answer": "1"
        },
        {
            "question": "Which of these methods is a part of Abstract Window Toolkit (AWT)?",
            "options": ["display()", "paint()", "drawString()", "transient()"],
            "correct_answer": "paint()"
        },
        {
            "question": "Which of these modifiers can be used for a variable so that it can be accessed from any thread or parts of a program?",
            "options": ["transient", "volatile", "global", "No modifier is needed"],
            "correct_answer": "volatile"
        },
        {
            "question": "A __________ control is a dialogue window that allows the user to pick a file?",
            "options": ["JChoosFile", "JFilefield", "JFile", "JFileChooser"],
            "correct_answer": "JFileChooser"
        },
        {
            "question": "Where are the following four methods commonly used?",
            "options": [
                "public void add(Component c)",
                "public void setSize(int width,int height)",
                "public void setLayout(LayoutManager m)",
                "public void setVisible(boolean)"
            ],
            "correct_answer": "public void setVisible(boolean)"
        },
        {
            "question": "_________ is a container for other components and is used to build bespoke panels for organizing and arranging components.",
            "options": ["JPanel", "JFrame", "JCombo", "JBox"],
            "correct_answer": "JPanel"
        },
        {
            "question": "Which of the following component gives a drop-down list of options from which to choose?",
            "options": ["JPanel", "JButton", "JComboBox", "JBox"],
            "correct_answer": "JComboBox"
        },
        {
            "question": "Which of these operators can be used to get run time information about an object?",
            "options": ["getInfo", "Info", "instanceof", "getinfoof"],
            "correct_answer": "instanceof"
        },
        {
            "question": "An _____________ is a short software that runs in a web browser.",
            "options": ["Application", "AWT", "Applet", "JFrame"],
            "correct_answer": "Applet"
        },
        {
            "question": "The act of turning the state of a Swing component or set of components into a stream of bytes that can be saved to a file or transferred over a network is referred to as ________ in Swing.",
            "options": ["Serialisation", "Accessibility", "Localization", "Globalization"],
            "correct_answer": "Serialisation"
        },
        {
            "question": "A ____ is a Swing framework component that offers a scroll bar that may be used to scroll content in a container.",
            "options": ["JScrollPanel", "JScrollBox", "JScroll", "JScrollBar"],
            "correct_answer": "JScrollBar"
        },
        {
            "question": "The ________ function is used to specify the layout of a container.",
            "options": ["UseLayeout()", "setLayout()", "layout()", "DesignLayout()"],
            "correct_answer": "setLayout()"
        }
    ]
} 