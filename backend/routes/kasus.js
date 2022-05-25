import express from "express";

import { 
    getAllKasus,
    addKasus,
    getKasusByUserId,
    getKasusById,
    updateKasus,
    getTime
} from "../controllers/Kasus.js";

// import { verifyToken } from "../middleware/VerifyToken.js";

const router = express.Router();

router.get('/',getAllKasus);
router.get('/date',getTime);
router.get('/user_id/:user_id',getKasusByUserId);
router.get('/:id',getKasusById);
router.post('/',addKasus);
router.patch('/:id',updateKasus);


export default router;