<template>
  <div>
    <Header />

    <section>
      <div class="container">
        <h1>
			{{project.name}}
		</h1>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
		return {
			project: {},
		}
  },
  async created() {
		try {
			const res = await this.$axios.get("/projects/"+ this.$route.params.id);
			console.log(res.data);
			
			this.project = res.data.project
		}
		catch (err) {
			console.log(err);
		}
	}
}
</script>

<style>

</style>