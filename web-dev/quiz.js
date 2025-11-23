// Simple JavaScript Quiz - External File

const quizQuestions = [
  { question: "What is the capital of india?", answer: "delhi" },
  { question: "What does HTML stand for?", answer: "hypertext markup language" },
  { question: "What is 2 + 2?", answer: "4" },
  { question: "Which language runs in the browser?", answer: "javascript" },
  { question: "CSS is used for?", answer: "styling" }
];

function runQuiz() {
  let score = 0;

  for (let i = 0; i < quizQuestions.length; i++) {
    let raw = prompt((i + 1) + ". " + quizQuestions[i].question);

    if (raw === null) {
      if (confirm("You pressed Cancel. Quit quiz?")) {
        alert("Quiz stopped. Score: " + score + "/" + quizQuestions.length);
        return;
      } else {
        raw = "";
      }
    }

    let userAnswer = String(raw).toLowerCase().trim();

    if (userAnswer === quizQuestions[i].answer) {
      score++;
      alert("Correct! ");
    } else {
      alert("Wrong  — correct answer: " + quizQuestions[i].answer);
    }
  }

  alert("Quiz Finished! Your score: " + score + " / " + quizQuestions.length);
}
