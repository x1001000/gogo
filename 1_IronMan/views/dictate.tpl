<div>
  <img id="start_button" onclick="startDictation(event)" src="https://avatars0.githubusercontent.com/u/6036508" width="100%">
</div>

<div id="results">
  <span id="final_span" class="final"></span>
  <span id="interim_span" class="interim"></span>
</div>

<script type="text/javascript">

var xhr = new XMLHttpRequest();

var final_transcript = '';
var recognizing = false;

if ('webkitSpeechRecognition' in window) {

  var recognition = new webkitSpeechRecognition();

  recognition.continuous = true;
  recognition.interimResults = true;

  recognition.onstart = function() {
    recognizing = true;
  };

  recognition.onerror = function(event) {
    console.log(event.error);
  };

  recognition.onend = function() {
xhr.open('GET', "/gogo/"+final_transcript, true);
xhr.send();
    recognizing = false;
  };

  recognition.onresult = function(event) {
    var interim_transcript = '';
// an event is a sentence    
    for (var i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        //final_transcript += event.results[i][0].transcript;
        final_transcript = event.results[i][0].transcript;
      } else {
        //interim_transcript += event.results[i][0].transcript;
        interim_transcript = event.results[i][0].transcript;
      }
    }
    //final_span.innerHTML = linebreak(final_transcript);
    //interim_span.innerHTML = linebreak(interim_transcript);
  };
}

var two_line = /\n\n/g;
var one_line = /\n/g;
function linebreak(s) {
  return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
}

function startDictation(event) {
  if (recognizing) {
    recognition.stop();
    return;
  }
  final_transcript = '';
  recognition.lang = 'cmn-Hant-TW';
  recognition.start();
  final_span.innerHTML = '';
  interim_span.innerHTML = '';
}
</script>