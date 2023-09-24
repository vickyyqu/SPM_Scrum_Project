import mysql from 'mysql';
 
const connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "sbrp_test"
})
 
export const getRoleListings = ()=>{
    connection.connect(function (err) {
        if (err) {
            console.log("Error in the connection")
            console.log(err)
        }
        else {
            console.log(`Database Connected`)
            connection.query(`SELECT * FROM Role_Listing`,
                function (err, result) {
                    if (err)
                        console.log(`Error executing the query - ${err}`)
                    else
                        console.log("Result: ", result)
                        return result
                })
        }
    });
}
getRoleListings()


// Connecting to database

// export const insertRole = (roleData, callback) => {
//     const sqlQuery = 'INSERT INTO your_table SET ?';
  
//     connection.query(sqlQuery, roleData, (error, results, fields) => {
//       if (error) {
//         return (error, null);
//       } else {
//         return results;
//       }
//     });
// };

