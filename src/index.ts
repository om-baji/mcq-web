import express from "express";
import { Question } from "../db/db";

const app = express();

app.get("/ques" , async (req, res) => {
    const ques = await Question.findOne({
        id : Math.floor(Math.random() * 25) + 1
    })
    console.log(ques)
})

app.listen(4000)