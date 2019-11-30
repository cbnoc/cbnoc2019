// RethinkDB Model
var thinky = require('thinky')();
var type = thinky.type;

var User = thinky.createModel("User", {
  id: type.string(),
  timestamp: type.string(),
  shost: type.string(),
  sIP: type.string(),
  dIP: type.string(),
  sPort: type.number(),
  dPort: type.number(),
  protocol: type.string(),
  login: type.string(),
  password: type.string(),
  hostname: type.string()
});

module.exports = User;
