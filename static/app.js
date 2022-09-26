$('#btnGuess').on('click', function (evt) {
  evt.preventDefault();
  const strWord = $('#word');
  //   alert(strWord.val());
  checkWord(strWord.val());
});

$('#btnStart').on('click', function () {
  document.location = '/start-game';
});

async function checkWord(word) {
  //   alert(word);
  let wordCheck = await axios.get('/check-word', { params: { word: word } });
  //   console.log(wordCheck.data);
  if (wordCheck.data === 'no') {
    $('#lblStatus').html('That is not a word!');
  } else if (wordCheck.data === 'ok') {
    $('#lblStatus').html('Great!');
    calculateScore(word);
  } else if (wordCheck.data === 'not-word') {
    $('#lblStatus').html('That is not a word!');
  } else if (wordCheck.data === 'not-on-board') {
    $('#lblStatus').html('That word is not on the board!');
  }
  $('#word').val('');
}

score = 0;
function calculateScore(word) {
  for (x = 0; x < word.length; x++) {
    score = score + 5;
  }
  $('#lblScore').html('Score : ' + score);
  //   alert(score);
}

time = 30;
function timer() {
  time = time - 1;
  if (time > 0) {
    $('#lblTimer').html(time + ' seconds left');
  } else {
    $('#lblTimer').html('Game Over!');
    $('#btnGuess').prop('disabled', true);
    $('#btnStartOver').prop('hidden', false);
    setHighscore(score);
    return false;
  }
  setTimeout(timer, 1000);
}
timer();

$('#btnStartOver').on('click', function (evt) {
  document.location = '/';
});

async function setHighscore(score) {
  let setHighscore = await axios.get('/set-highscore', {
    params: { score: score },
  });
  // console.log(setHighscore.data);
}
async function setCount(times_visited) {
  const obj = { times_visited: times_visited };

  const request = new Request('/count', {
    method: 'POST',
    body: JSON.stringify(obj),
  });

  request.json().then((data) => {
    console.log(data.times_visited);
  });
}

$('#btnPost').on('click', function (evt) {
  evt.preventDefault();
  setCount(12);
});
