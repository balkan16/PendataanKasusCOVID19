import express from "express";

import { 
    getAllKasus,
    addKasus,
    getKasusByUserId,
    getKasusById,
    updateKasus,
} from "../controllers/Kasus.js";

// import {
//     getUsers,
//     Register
// } from "../controllers/Users.js";

const router = express.Router();

router.get('/',getAllKasus);
router.get('/user_id/:user_id',getKasusByUserId);
router.get('/:id',getKasusById);
router.post('/',addKasus);
router.patch('/:id',updateKasus);
// router.get('/users',getUsers);
// router.post('/users',Register);

export default router;