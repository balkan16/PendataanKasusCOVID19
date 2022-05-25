import express from "express";

import {
    getUsers,
    getUsersById,
    updateUsers,
    Register,
    Login,
    Logout
} from "../controllers/Users.js";

// import { verifyToken } from "../middleware/VerifyToken.js";
import { refreshToken } from "../controllers/RefreshToken.js";

const router = express.Router();

router.get('/',getUsers);
router.get('/:id',getUsersById);
router.post('/',Register);
router.post('/login',Login);
router.get('/token',refreshToken);
router.delete('/logout',Logout);
router.patch('/:id',updateUsers);

export default router;