const mongoose = require('mongoose');

mongoose
    .connect("mongodb://127.0.0.1:27017/")
        .then( () => {
            console.log("DB connected!")
        })
        .catch( e => {
            console.log("Internal server error!")
        })

const questionSchema = new mongoose.Schema({
    question : String,
    options : [String],
    correct_answer : String
})

const Question = mongoose.model("Question" , questionSchema);

module.exports = {
    Question
}