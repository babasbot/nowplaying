# NowPlaying

**NowPlaying** is a server that broadcasts your current song from the Last.FM
API to a websocket. 

## Getting Started 

Define the following envs with your last.fm API keys. If you don't own an API 
key, you can apply for one [here](https://www.last.fm/api/account/create).

```sh
export PYLAST_API_KEY=API_KEY
export PYLAST_API_SECRET=SECRET_KEY
```

Start the websocket server with the following command:

```sh
python ./nowplaying/server.py your_lastfm_username
```

### Send Now Playing messages on Mixlr

You can send *"now playing"* messages to a Mixlr live page from the **NowPlaying**
server. Open your browser's Javascript console at the Mixlr's live page and run
the following script:

```Javascript
var socket = new WebSocket("ws://localhost:8080/");
socket.onmessage = function (event) {
  $("#chat_box form fieldset textarea").val(event.data);
  $("#chat_box form fieldset button").click()
}
```

Now each time you play a new track, your browser will send a "now playing" message
like this one:

![nowplaying](https://user-images.githubusercontent.com/764518/39400542-e808d26a-4af7-11e8-93c0-84b85309a5a5.png)

## Authors

* **Luis Alfredo Lorenzo** - [babasbot](https://github.com/babasbot)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
