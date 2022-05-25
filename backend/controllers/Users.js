import Users from "../models/userModel.js"
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

export const getUsers = async (req,res) => {
    try{
        const users = await Users.findAll();
        res.json(users);
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const getUsersById = async (req,res) => {
    try{
        const users = await Users.findAll({
            where:{
                id: req.params.id
            }
        });
        res.json(users);
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const updateUsers = async (req,res) => {
    try{
        await Users.update(req.body,{
            where:{
                id: req.params.id
            }
        });
        res.json({
            "message": "Data User Berhasil Diperbarui"
        });
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const Register = async(req,res) => {
    try{
        const { name, email, kota, password, confPassword } = req.body;
        if(password !== confPassword) return res.status(400).json({
            message: "Konfirmasi Password tidak sama"
        });
        const salt = await bcrypt.genSalt();
        const hashPassword = await bcrypt.hash(password, salt);
        try{
            await Users.create({
                name: name,
                email: email,
                kota: kota,
                password: hashPassword
            });
            res.json({msg: "Akun berhasil didaftarkan"})
        } catch (error) {
            res.json({ message: error.message});
        }
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const Login = async(req,res) => {
    try{
        const user = await Users.findAll({
            where:{
                email: req.body.email
            }
        });
        const match = await bcrypt.compare(req.body.password, user[0].password);
        if(!match) return res.status(400).json({msg: "Password Anda Salah"});
        const userId = user[0].id;
        const name = user[0].name;
        const email = user[0].email;
        const kota = user[0].kota;
        const accessToken = jwt.sign({userId, name, email}, process.env.ACCESS_TOKEN_SECRET,{
            expiresIn: '1d'
        });
        const refreshToken = jwt.sign({userId, name, email}, process.env.REFRESH_TOKEN_SECRET,{
            expiresIn: '1d'
        });
        await Users.update({refresh_token: refreshToken},{
            where:{
                id: userId
            }
        });
        res.cookie('refreshToken',refreshToken,{
            httpOnly: true,
            maxAge: 24 * 60 * 60 * 1000
        });
        res.json({ userId });
    } catch (error){
        res.status(404).json({msg:"Email tidak ditemukan"})
    }
}
 
export const Logout = async(req,res)=>{
    const refreshToken = req.cookies.refreshToken;
    if(!refreshToken) return res.sendStatus(204); //No Content
        const user = await Users.findAll({
            where:{
                refresh_token: refreshToken
            }
        });
        if(!user[0]) return res.sendStatus(204); //No Content
    const userId = user[0].id;
    await Users.update({refresh_token: null},{
        where:{
            id: userId
        }
    });
    res.clearCookie('refreshToken');
    return res.sendStatus(200);
} 
