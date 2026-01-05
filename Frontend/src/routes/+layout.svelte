<script lang="ts">
	import './layout.css';
	let { children } = $props();
</script>

<svelte:head>
	<title>Paix</title>
</svelte:head>

<main class="font-primary-main">
	<section>
		{@render children()}
	</section>
</main>
