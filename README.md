# ipp_server_flask

This library implements an IPP print server (eg. pretend printer) using Flask. 

It is based on the [ipp-server](https://github.com/h2g2bob/ipp-server) but is ultimately designed to be more modern, more extensible and to be importable as a module. 

The key reason for the change is to support authentication. 

# Roadmap 

The MVP will offer roughly the same functionality as the `ipp-server` library. It probably won't work as nicely but it will work. 

The most critical feature to implement will be authentication, alongside tidying up and fixing stuff. 

I am open to Issues with suggestions :-) 