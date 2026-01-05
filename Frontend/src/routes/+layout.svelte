<script lang="ts">
	import './layout.css';
	let { children } = $props();
</script>

<svelte:head>
	<title>Paix</title>
</svelte:head>

<main class="font-primary-main bg-gray-200">
	<section>
		{@render children()}
	</section>
</main>
