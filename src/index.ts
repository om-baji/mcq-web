import express from "express";
import { Question } from "../db/db";

const app = express();

app.use(express.json());

app.get("/ques" , async (req, res) => {
    const ques = await Question.findOne({
        number : Math.floor(Math.random() * 25) + 1
    })
    res.json({
        question : ques?.question,
        options : ques?.options
    })
})

app.listen(4000)