echo "Please fill in the following information:"
if [ -z "$1" ]; then
    read -p "Prefix of the bot: " prefix
else
    prefix=$1
fi

if [ -z "$2" ]; then
    read -p "The bot's token: " token
else
    token=$2
fi

echo "Creating config file..."
echo "PREFIX=$prefix
TOKEN=$token" > .env