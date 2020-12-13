<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
     Backend message:
     {{ message }}
    </p>
  </div>
</template>

<script>
let axios = require('axios');


export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data: function () {
    return {
      message: 'Nothing'
    }
  },
  created: function () {
    axios.get('http://127.0.0.1:8001/api_test/')
    .then((response) => {
      // handle success 
      this.message = response.data.data;
    })
    .catch((error) => {
      // handle error
      console.log(error);
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
