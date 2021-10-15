const Discord = require("discord.js"); // Requires the npm package 'discord.js'.
const client = new Discord.Client(); // Create an instance of Discord#Client
const config = require("./config.json");
client.login(config.token); // Uses value of key 'token' in config file.

client.on("message", (message) => {
if(message.content == "!ping"){ // Check if content of message is "!ping"
		message.channel.send("pong!"); // Call .send() on the channel object the message was sent in
	}
if("guildMemberAdd", (member) => { // EventEmitter, nothing new
        message.channel.send("HI!")
    }
});

