import mongoose from "mongoose";

mongoose
    .connect("mongodb://127.0.0.1:27017/cpp_mcq_db")
        .then( () => {
            console.log("DB connected!")
        })
        .catch( e => {
            console.log("Internal server error!")
        })

const questionSchema = new mongoose.Schema({
    number : Number,
    question : String,
    options : [String],
    correct_answer : String
})

export const Question = mongoose.model("Question" , questionSchema);
