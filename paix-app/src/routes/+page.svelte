<script lang="ts">
  let message: string = $state("Blessings");

  const handleMessage = () => {
    console.log(message);
    message = "James Gama"
  }
</script>

<section>
  <div>
    <h1>This is the start of working with my app mate</h1>
    <p>{message}</p>
    <button onclick="{handleMessage}" aria-label="button">
      <span class="">click me</span>
    </button>
  </div>
</section>