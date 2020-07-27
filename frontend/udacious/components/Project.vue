<template>
  <nuxt-link :to="'/' + details.id" class="project link">
    <div class="col s4">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="~assets/office.jpg" />
          </div>
          <div class="card-content">
            <span class="card-title activator grey-text text-darken-4"
              >{{ details.name }}<i class="material-icons right">more_vert</i></span
            >
            <div class="row">
              <p class="col s6">Student id: {{ details.student_id }}</p>
              <p class="col s6">Duration: {{ details.project_duration }} day<span v-if="details.project_duration > 1">s</span></p>
            </div>
          </div>
          <div class="card-reveal">
            <span class="card-title grey-text text-darken-4"
              >{{ details.name }}<i class="material-icons right">close</i></span
            >
            <p>
              {{ details.description }}
            </p>
          </div>
        </div>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  name: "Project",
  props: ["details"]
};
</script>

<style>
.card-image img {
  width: 100% !important;
  height: 300px !important;
  object-fit: cover;
  object-position: center;
}

a.link{
  color: inherit !important;
  /* font-weight: 500; */
}

.card {
  overflow: hidden !important;
}

.card .card-reveal {
  display: block !important;
  /* background: rgba(255, 255, 255, 0.9) !important; */
  transition: all ease-in-out 500ms !important;
}

.card:hover .card-reveal {
  display: block !important;
  transform: translateY(-70%) !important;
}
</style>
