<script lang="ts">
	let { children } = $props();
</script>


<main class="min-h-screen">
	<nav class="fixed w-72 px-2 py-2 bg-white h-full overflow-auto">
		<div class="site__logo">
			<h1 class="font-extrabold text-3xl uppercase">paix</h1>
		</div>

		<div class="py-7">
			<div>
				<ul class="flex flex-col gap-2">
					<li class="hover:bg-gray-100 py-2 px-2 rounded-xl">
						<a href="/" class="flex items-center gap-1">
							<span class="icon-[tabler--home] text-xl"></span>
							<span class="capitalize">home</span>
						</a>
					</li>

					<li class="hover:bg-gray-100 py-2 px-2 rounded-xl">
						<a href="/" class="flex items-center gap-1">
							<span class="icon-[tabler--blocks] text-xl"></span>
							<span class="capitalize">projects</span>
						</a>
					</li>

					<li class="hover:bg-gray-100 py-2 px-2 rounded-xl">
						<a href="/" class="flex items-center gap-1">
							<span class="icon-[tabler--files] text-xl"></span>
							<span class="capitalize">file manager</span>
						</a>
					</li>

					<li class="hover:bg-gray-100 py-2 px-2 rounded-xl">
						<a href="/" class="flex items-center gap-1">
							<span class="icon-[tabler--books] text-xl"></span>
							<span class="capitalize">structure</span>
						</a>
					</li>

					<li class="hover:bg-gray-100 py-2 px-2 rounded-xl">
						<a href="/" class="flex items-center gap-1">
							<span class="icon-[tabler--pin] text-xl"></span>
							<span class="capitalize">pinned projects</span>
						</a>
					</li>

					<li class="hover:bg-gray-100 py-2 px-2 rounded-xl">
						<a href="/" class="flex items-center gap-1">
							<span class="icon-[tabler--user-heart] text-xl"></span>
							<span class="capitalize">wellbeing</span>
						</a>
					</li>

					<li class="hover:bg-gray-100 py-2 px-2 rounded-xl">
						<a href="/" class="flex items-center gap-1">
							<span class="icon-[tabler--settings] text-xl"></span>
							<span class="capitalize">settings</span>
						</a>
					</li>

				</ul>
			</div>
		</div>
	</nav>

	<section class="ps-72">
		{@render children()}
	</section>
</main>

