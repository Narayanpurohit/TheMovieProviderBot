# Existing imports remain the same
from aiohttp import web
import ssl  # Add SSL module for handling certificates

# Paths to your SSL certificate and private key
SSL_CERT_PATH = '/www/server/panel/vhost/cert/st.jnmovies.site/fullchain.pem'
SSL_KEY_PATH = '/www/server/panel/vhost/cert/st.jnmovies.site/privkey.pem'

async def Lazy_start():
    print('\n')
    print('Initalizing The Movie Provider Bot')
    bot_info = await LazyPrincessBot.get_me()
    LazyPrincessBot.username = bot_info.username
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("The Movie Provider Imported => " + plugin_name)
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    me = await LazyPrincessBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    LazyPrincessBot.username = '@' + me.username
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    logging.info(script.LOGO)
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await LazyPrincessBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    
    # Initialize the web server with SSL
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    
    # Configure SSL context
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(SSL_CERT_PATH, SSL_KEY_PATH)
    
    # Start the web server with SSL
    await web.TCPSite(app, bind_address, PORT, ssl_context=ssl_context).start()
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(Lazy_start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')









