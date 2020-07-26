<template>
  <div>
    <Header />
    <section id="hero">
      <div class="container center-align">
        <h1>Join the Clique</h1>
        <p>Discover inspiring projects from udacity students around the world.</p>
        <a href="#projects" class="light-blue accent-4 waves-effect btn padd-1">See Projects</a>
      </div>
    </section>

    <section id="projects">
      <div class="container">
        <div class="row">

          <div class="col s4">
            <div class="card">
              <div class="card-image waves-effect waves-block waves-light">
                <img class="activator" src="~assets/office.jpg">
              </div>
              <div class="card-content">
                <span class="card-title activator grey-text text-darken-4">Card Title<i class="material-icons right">more_vert</i></span>
                <p><a href="#">This is a link</a></p>
              </div>
              <div class="card-reveal">
                <span class="card-title grey-text text-darken-4">Card Title<i class="material-icons right">close</i></span>
                <p>Here is some more information about this product that is only revealed once clicked on.</p>
              </div>
            </div>
          </div>
          <div class="col s4">
            <div class="card">
              <div class="card-image waves-effect waves-block waves-light">
                <img class="activator" src="~assets/office.jpg">
              </div>
              <div class="card-content">
                <span class="card-title activator grey-text text-darken-4">Card Title<i class="material-icons right">more_vert</i></span>
                <p><a href="#">This is a link</a></p>
              </div>
              <div class="card-reveal">
                <span class="card-title grey-text text-darken-4">Card Title<i class="material-icons right">close</i></span>
                <p>Here is some more information about this product that is only revealed once clicked on.</p>
              </div>
            </div>
          </div>
          <div class="col s4">
            <div class="card">
              <div class="card-image waves-effect waves-block waves-light">
                <img class="activator" src="~assets/office.jpg">
              </div>
              <div class="card-content">
                <span class="card-title activator grey-text text-darken-4">Card Title<i class="material-icons right">more_vert</i></span>
                <p><a href="#">This is a link</a></p>
              </div>
              <div class="card-reveal">
                <span class="card-title grey-text text-darken-4">Card Title<i class="material-icons right">close</i></span>
                <p>Here is some more information about this product that is only revealed once clicked on.</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {}
</script>

<style>
:root {
  scroll-behavior: smooth;
}

.container {
  width: 90%;
  margin: auto;
}

p {
  max-width: 850px;
  margin-left: auto;
  margin-right: auto;
}

#hero {
  font-size: 1.3em;
  padding: 6em 0;
  /* bg */
}

#hero h1 {
  font-size: 4em;
  margin-top: 0;
  color: transparent;
  background: linear-gradient(to right, rgb(74 146 234), #004b2e);
  -webkit-background-clip: text;
  animation: hue-rotate 4s linear infinite;
  /* filter: hue-rotate(100deg); */
}

#hero a[href *= projects] {
  margin-top: 2em;
}

@keyframes hue-rotate {
  100% {
    /* filter: hue-rotate(360deg) */
  }
}

</style>
