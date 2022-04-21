import { Sequelize } from "sequelize";

const db = new Sequelize('metn_db','root','',{
    host: "localhost",
    dialect: "mysql",
}) 

export default db;

