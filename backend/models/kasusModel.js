import { Sequelize } from "sequelize";
import db from "../config/database.js";

const { DataTypes } = Sequelize;

const Kasus = db.define('kasus',{
    positif:{
        type: DataTypes.INTEGER
    },
    meninggal:{
        type: DataTypes.INTEGER
    },
    sembuh:{
        type: DataTypes.INTEGER
    },
    user_id:{
        type: DataTypes.INTEGER
    },
    tanggal:{
        type: DataTypes.DATEONLY
    }
},{
    freezeTableName: true
});

export default Kasus;