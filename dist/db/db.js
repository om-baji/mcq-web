"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Question = void 0;
const mongoose_1 = __importDefault(require("mongoose"));
mongoose_1.default
    .connect("mongodb://127.0.0.1:27017/cpp_mcq_db")
    .then(() => {
    console.log("DB connected!");
})
    .catch(e => {
    console.log("Internal server error!");
});
const questionSchema = new mongoose_1.default.Schema({
    number: Number,
    question: String,
    options: [String],
    correct_answer: String
});
exports.Question = mongoose_1.default.model("Question", questionSchema);
