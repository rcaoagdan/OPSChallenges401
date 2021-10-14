-- HEAD -- 

description = [[
NAME: RAY CAOAGDAN
DATE: 10/14/2021
PURPOSE: Practice NSE SCRIPT
SOURCE: https://null-byte.wonderhowto.com/how-to/get-started-writing-your-own-nse-scripts-for-nmap-0187403/
]]
 
-- RULE --

portrule = function(host, port)
	return port.portocol == "tcp"
		and port.state == "open"

end

-- ACTION --

action = function (host, port)
	return "OPEN PORT FOUND!!!"

end