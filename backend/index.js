import express from "express";
import db from "./config/database.js";
import dotenv from "dotenv";

import kasusRoutes from "./routes/kasus.js";
import userRoutes from "./routes/users.js";
import Users from "./models/userModel.js"
dotenv.config();

import cookieParser from "cookie-parser";

import cors from "cors";

const app = express();

try{
    await db.authenticate();
    console.log('Database connected...');
    // await Users.sync();
} catch (error){
    console.error('Connection error:',error);
}

app.use(cors({ 
    credentials: true,
    origin:'http://localhost:5000'}));
app.use(express.json());
app.use(cookieParser());
// app.use( bodyParser.json() );
app.use('/kasus',kasusRoutes);
app.use('/users',userRoutes);
app.listen(5000, () => console.log('Server running at port 5000'));