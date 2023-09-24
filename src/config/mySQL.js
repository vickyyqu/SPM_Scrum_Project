import mysql from 'mysql';
 
const connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "sbrp_test"
})
 
// Connecting to database
connection.connect(function (err) {
    if (err) {
        console.log("Error in the connection")
        console.log(err)
    }
    else {
        console.log(`Database Connected`)
    //     connection.query(`SELECT * FROM Role_Listing`,
    //         function (err, result) {
    //             if (err)
    //                 console.log(`Error executing the query - ${err}`)
    //             else
    //                 console.log("Result: ", result)
    //         })
    }
});

export default connection

