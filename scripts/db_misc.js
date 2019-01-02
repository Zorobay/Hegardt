const mongoose = require('mongoose');
const Person = mongoose.model('Person');

let findByName = function(name) {
    const query = [{first_name: {$regex: "seb", $options: i}}];
    console.log("hej!")
    Person.find({first_name: "Sebastian"}, function(err, res){
       console.log(res);
    });
}