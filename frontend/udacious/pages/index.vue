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

          <Project v-for="project in projects" :key="project.id" :details='project' />
					
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Project from '../components/Project';

export default {	
  components: {
    Project 
  },
	data() {
		return {
			projects: []
		}
	},
	mounted() {
	},
	async created() {
		try {
			const res = await this.$axios.get("/projects");
			console.log(res.data);
			
			this.projects = res.data.projects
		}
		catch (err) {
			console.log(err);
		}
	}
}
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
  background-clip: text;
  /* animation: hue-rotate 10s linear infinite; */
}

#hero a[href *= projects] {
  margin-top: 2em;
}

@keyframes hue-rotate {
  100% {
    filter: hue-rotate(360deg)
  }
}

</style>
