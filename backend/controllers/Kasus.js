import Kasus from "../models/kasusModel.js"


export const getAllKasus = async (req,res) => {
    try{
        const kasus = await Kasus.findAll();
        res.json(kasus);
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const addKasus = async (req,res) => {
    try{
        const kasus = await Kasus.create(req.body);
        res.json({
            "message": "Kasus Berhasil Ditambahkan"
        });
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const getKasusByUserId = async (req,res) => {
    try{
        const kasus = await Kasus.findAll({
            where:{
                user_id: req.params.user_id,
                tanggal: req.body
            }
        });
        res.json(kasus);
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const getKasusById = async (req,res) => {
    try{
        const kasus = await Kasus.findAll({
            where:{
                id: req.params.id,
            }
        });
        res.json(kasus);
    } catch (error) {
        res.json({ message: error.message});
    }
}

// export const getKasusByIdDate = async (req,res) => {
//     try{
//         const kasus = await Kasus.findAll({
//             where:{
//                 id: req.params.id
//                 date: req.body
//             }
//         });
//         res.json(kasus);
//     } catch (error) {
//         res.json({ message: error.message});
//     }
// }

export const updateKasus = async (req,res) => {
    try{
        await Kasus.update(req.body,{
            where:{
                id: req.params.id
            }
        });
        res.json({
            "message": "Data Kasus Berhasil Diperbarui"
        });
    } catch (error) {
        res.json({ message: error.message});
    }
}

export const getTime = async (req,res) => {
    var todayDate = new Date();
    todayDate.setMinutes(todayDate.getMinutes() - todayDate.getTimezoneOffset()); 
    todayDate = todayDate.toISOString().slice(0,10); 
    console.log(todayDate);
    res.send(todayDate);
}