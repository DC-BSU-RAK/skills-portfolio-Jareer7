"""
01-MAth Quiz

A math quiz game with three difficulty levels.
Users answer 10 questions and get scored based on their performance.
"""

import tkinter as tk
from tkinter import messagebox
import random

class MathsQuiz:
    """Main quiz class"""
    
    def __init__(self, root):
        """Setup the main window"""
        self.root = root
        self.root.title("Jareer's Mathematical Challenge Quiz")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.config(bg='#1a1a2e')
        
        # Variables to track quiz state
        self.difficulty = ""
        self.score = 0
        self.question_num = 0
        self.total_questions = 10
        self.attempt_count = 0
        self.correct_ans = 0
        self.number1 = 0
        self.number2 = 0
        self.math_operation = ""
        self.questions_data = []
        
        # Show the main menu
        self.display_menu()
    
    def clear_window(self):
        """Clear everything from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def display_menu(self):
        """Show the main menu with difficulty options"""
        self.clear_window()
        
        # Main background
        main_frame = tk.Frame(self.root, bg='#16213e')
        main_frame.pack(fill='both', expand=True)
        
        # Top section
        header_frame = tk.Frame(main_frame, bg='#0f3460', height=120)
        header_frame.pack(fill='x', pady=(0, 20))
        
        # Title
        title = tk.Label(
            header_frame,
            text="📊 MATHEMATICAL CHALLENGE QUIZ",
            font=('Courier New', 28, 'bold'),
            fg='#00d9ff',
            bg='#0f3460'
        )
        title.pack(pady=30)
        
        # Welcome text
        welcome_msg = tk.Label(
            main_frame,
            text="Test your arithmetic skills!",
            font=('Arial', 16),
            fg='#ffffff',
            bg='#16213e'
        )
        welcome_msg.pack(pady=10)
        
        subtitle = tk.Label(
            main_frame,
            text="Select your challenge level to begin",
            font=('Arial', 12),
            fg='#94a3b8',
            bg='#16213e'
        )
        subtitle.pack(pady=5)
        
        # Container for buttons
        buttons_frame = tk.Frame(main_frame, bg='#16213e')
        buttons_frame.pack(pady=30)
        
        # Three difficulty levels
        difficulty_info = [
            ("🟢 EASY MODE", "Addition & Subtraction (1-9)", "easy", '#10b981'),
            ("🟡 MODERATE MODE", "Addition & Subtraction (10-99)", "moderate", '#f59e0b'),
            ("🔴 HARD MODE", "Multiplication (1-12)", "hard", '#ef4444')
        ]
        
        # Create each button
        for title_text, desc, level, btn_color in difficulty_info:
            container = tk.Frame(buttons_frame, bg='#16213e')
            container.pack(pady=15)
            
            # Button
            btn = tk.Button(
                container,
                text=title_text,
                font=('Arial', 15, 'bold'),
                bg=btn_color,
                fg='white',
                width=30,
                height=2,
                relief='flat',
                cursor='hand2',
                command=lambda lv=level: self.start_quiz(lv)
            )
            btn.pack()
            
            # Description
            desc_label = tk.Label(
                container,
                text=desc,
                font=('Arial', 10),
                fg='#94a3b8',
                bg='#16213e'
            )
            desc_label.pack(pady=3)
        
        # Bottom text
        footer = tk.Label(
            main_frame,
            text="⏱ 10 Questions | 🎯 100 Points Maximum",
            font=('Arial', 10),
            fg='#64748b',
            bg='#16213e'
        )
        footer.pack(side='bottom', pady=20)
    
    def start_quiz(self, difficulty):
        """Start the quiz with chosen difficulty"""
        self.difficulty = difficulty
        self.score = 0
        self.question_num = 0
        self.questions_data = []
        
        # Create all 10 questions
        for i in range(self.total_questions):
            num1, num2 = self.random_int()
            operation = self.decide_operation()
            
            # Calculate answer
            if operation == '+':
                answer = num1 + num2
            elif operation == '-':
                answer = num1 - num2
            else:  # multiplication
                answer = num1 * num2
            
            # Store question
            self.questions_data.append({
                'num1': num1,
                'num2': num2,
                'operation': operation,
                'answer': answer
            })
        
        # Show first question
        self.display_problem()
    
    def random_int(self):
        """Generate random numbers based on difficulty"""
        if self.difficulty == "easy":
            return random.randint(1, 9), random.randint(1, 9)
        elif self.difficulty == "moderate":
            return random.randint(10, 99), random.randint(10, 99)
        else:  # hard
            return random.randint(1, 12), random.randint(1, 12)
    
    def decide_operation(self):
        """Choose the operation type"""
        if self.difficulty == "hard":
            return '×'  # Multiplication for hard mode
        else:
            return random.choice(['+', '-'])  # Addition or subtraction
    
    def display_problem(self):
        """Show a math question"""
        # Check if quiz is done
        if self.question_num >= self.total_questions:
            self.display_results()
            return
        
        self.clear_window()
        
        # Get current question
        current_q = self.questions_data[self.question_num]
        self.number1 = current_q['num1']
        self.number2 = current_q['num2']
        self.math_operation = current_q['operation']
        self.correct_ans = current_q['answer']
        self.attempt_count = 0
        
        # Colors for each difficulty
        difficulty_colors = {
            'easy': '#10b981',
            'moderate': '#f59e0b',
            'hard': '#ef4444'
        }
        
        current_color = difficulty_colors.get(self.difficulty, '#00d9ff')
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#16213e')
        main_frame.pack(fill='both', expand=True)
        
        # Top section
        header = tk.Frame(main_frame, bg='#0f3460', height=80)
        header.pack(fill='x')
        
        # Question number
        progress_text = f"Question {self.question_num + 1} of {self.total_questions}"
        progress = tk.Label(
            header,
            text=progress_text,
            font=('Arial', 13),
            fg='#94a3b8',
            bg='#0f3460'
        )
        progress.pack(pady=10)
        
        # Score
        score_display = tk.Label(
            header,
            text=f"Current Score: {self.score} / 100",
            font=('Arial', 16, 'bold'),
            fg='#00d9ff',
            bg='#0f3460'
        )
        score_display.pack(pady=5)
        
        # Question box
        question_card = tk.Frame(main_frame, bg='#1e293b', relief='ridge', bd=3)
        question_card.pack(pady=40, padx=60, fill='both', expand=True)
        
        # Difficulty label
        badge = tk.Label(
            question_card,
            text=self.difficulty.upper(),
            font=('Arial', 10, 'bold'),
            fg='white',
            bg=current_color,
            padx=15,
            pady=5
        )
        badge.pack(pady=(20, 10))
        
        # The math problem
        problem_text = f"{self.number1}  {self.math_operation}  {self.number2}  ="
        problem = tk.Label(
            question_card,
            text=problem_text,
            font=('Courier New', 40, 'bold'),
            fg='#ffffff',
            bg='#1e293b'
        )
        problem.pack(pady=30)
        
        # Input box
        self.answer_var = tk.StringVar()
        answer_entry = tk.Entry(
            question_card,
            textvariable=self.answer_var,
            font=('Arial', 24),
            width=12,
            justify='center',
            relief='solid',
            bd=2,
            bg='#334155',
            fg='white',
            insertbackground='white'
        )
        answer_entry.pack(pady=20)
        answer_entry.focus()
        
        # Submit button
        submit_btn = tk.Button(
            question_card,
            text="SUBMIT ANSWER",
            font=('Arial', 14, 'bold'),
            bg='#00d9ff',
            fg='#1a1a2e',
            width=20,
            height=2,
            relief='flat',
            cursor='hand2',
            command=self.check_answer
        )
        submit_btn.pack(pady=15)
        
        # Press Enter to submit
        answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # Feedback text
        self.feedback_msg = tk.Label(
            question_card,
            text="",
            font=('Arial', 12, 'bold'),
            bg='#1e293b'
        )
        self.feedback_msg.pack(pady=10)
    
    def check_answer(self):
        """Check if the answer is a valid number"""
        try:
            user_input = int(self.answer_var.get())
            self.is_correct(user_input)
        except ValueError:
            self.feedback_msg.config(
                text="⚠ Please enter a valid number!",
                fg='#f59e0b'
            )
    
    def is_correct(self, user_answer):
        """Check if answer is correct and update score"""
        if user_answer == self.correct_ans:
            # Correct answer
            if self.attempt_count == 0:
                # First try - 10 points
                self.score += 10
                self.feedback_msg.config(
                    text="✓ CORRECT! +10 Points",
                    fg='#10b981'
                )
            else:
                # Second try - 5 points
                self.score += 5
                self.feedback_msg.config(
                    text="✓ CORRECT! +5 Points",
                    fg='#10b981'
                )
            
            # Go to next question
            self.question_num += 1
            self.root.after(1200, self.display_problem)
        else:
            # Wrong answer
            self.attempt_count += 1
            
            if self.attempt_count == 1:
                # First try wrong - try again
                self.feedback_msg.config(
                    text="✗ Incorrect! Try again (5 points available)",
                    fg='#ef4444'
                )
                self.answer_var.set("")
            else:
                # Second try wrong - move on
                self.feedback_msg.config(
                    text=f"✗ Incorrect! Answer was {self.correct_ans}",
                    fg='#ef4444'
                )
                self.question_num += 1
                self.root.after(2000, self.display_problem)
    
    def display_results(self):
        """Show final score and grade"""
        self.clear_window()
        
        # Calculate grade
        if self.score >= 90:
            grade = "A+"
            message = "Outstanding Performance! 🌟"
            grade_color = '#10b981'
        elif self.score >= 80:
            grade = "A"
            message = "Excellent Work! 🎯"
            grade_color = '#10b981'
        elif self.score >= 70:
            grade = "B"
            message = "Good Job! 👍"
            grade_color = '#3b82f6'
        elif self.score >= 60:
            grade = "C"
            message = "Keep Practicing! 📚"
            grade_color = '#f59e0b'
        else:
            grade = "D"
            message = "Try Again! 💪"
            grade_color = '#ef4444'
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#16213e')
        main_frame.pack(fill='both', expand=True)
        
        # Top section
        header = tk.Frame(main_frame, bg='#0f3460', height=100)
        header.pack(fill='x')
        
        completion_text = tk.Label(
            header,
            text="🎊 QUIZ COMPLETED 🎊",
            font=('Courier New', 26, 'bold'),
            fg='#00d9ff',
            bg='#0f3460'
        )
        completion_text.pack(pady=30)
        
        # Results box
        results_card = tk.Frame(main_frame, bg='#1e293b', relief='ridge', bd=3)
        results_card.pack(pady=30, padx=80, fill='both', expand=True)
        
        # Final score
        score_label = tk.Label(
            results_card,
            text=f"Final Score: {self.score} / 100",
            font=('Arial', 32, 'bold'),
            fg='#00d9ff',
            bg='#1e293b'
        )
        score_label.pack(pady=(40, 20))
        
        # Grade
        grade_label = tk.Label(
            results_card,
            text=f"Grade: {grade}",
            font=('Arial', 28, 'bold'),
            fg=grade_color,
            bg='#1e293b'
        )
        grade_label.pack(pady=15)
        
        # Message
        message_label = tk.Label(
            results_card,
            text=message,
            font=('Arial', 18),
            fg='#94a3b8',
            bg='#1e293b'
        )
        message_label.pack(pady=15)
        
        # Buttons
        buttons_frame = tk.Frame(results_card, bg='#1e293b')
        buttons_frame.pack(pady=30)
        
        # Play again
        replay_btn = tk.Button(
            buttons_frame,
            text="🔄 PLAY AGAIN",
            font=('Arial', 14, 'bold'),
            bg='#00d9ff',
            fg='#1a1a2e',
            width=18,
            height=2,
            relief='flat',
            cursor='hand2',
            command=self.display_menu
        )
        replay_btn.pack(side='left', padx=10)
        
        # Exit
        exit_btn = tk.Button(
            buttons_frame,
            text="❌ EXIT",
            font=('Arial', 14, 'bold'),
            bg='#ef4444',
            fg='white',
            width=18,
            height=2,
            relief='flat',
            cursor='hand2',
            command=self.root.quit
        )
        exit_btn.pack(side='left', padx=10)


# Run the program
if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = MathsQuiz(root)
    root.mainloop()