<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>task2</title>
  </head>
  <body>
    <div id="result"></div>
    <button id="btn_get">run a get data</button>
    <script>
      const api_url = 'https://www.amiiboapi.com/api/amiibo/?name=mario'
      function update_data(response_data) {
        result.appendChild(document.createTextNode(Object.keys(response_data)))
        result.appendChild(document.createElement('br'))
      }
      btn_get.addEventListener('click', async function () {
        const response = await fetch(api_url)
        if (response.ok) {
          const response_data = await response.json()
          update_data(response_data)
        } else {
          console.log(response)
          console.error('HTTP-error' + response.status)
        }
      })
    </script>
  </body>
</html>

