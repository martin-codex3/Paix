<script lang="ts">

	let { children } = $props();

</script>


<main class="min-h-screen">
	<nav class="fixed w-72 px-3 py-2 bg-white h-full">
		<div class="site__logo">
			<h1 class="font-extrabold text-3xl uppercase">paix</h1>
		</div>

		<div class="py-7">
			<div>
				<ul class="flex flex-col gap-5">
					<li>
						<a href="/" class="flex items-center h-5 gap-1 text-xl">
							<span class="icon-[tabler--home]"></span>
							<span class="capitalize text-lg">home</span>
						</a>
					</li>
				</ul>
			</div>
		</div>
	</nav>

	<section class="col-span-10 px-5">
		{@render children()}
	</section>
</main>

