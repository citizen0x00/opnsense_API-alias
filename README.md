# opnsense_API-alias
Adding IP to alias through a pythonscript

## Preparing the script
Create an API-user by adding an account in the usersection on OPNSense and creating API-keys. You need both key and secretkey. Add those in the script.
Change the variable "opnsense" to match your opnsense IP.

## Running the script
```python app.py -ip <Your IP to add>```
## Running the script with the --alias argument
In the configsection:
```
#alias = "" #The alias you want to add the IP to
alias = args.alias #uncomment out this if you want alias to hardcode the alias
```
Run the script with the alias-argument:
```python app.py -ip <Your IP to add> -a MyAlias```
```python app.py -ip <Your IP to add> --alias MyAlias```
