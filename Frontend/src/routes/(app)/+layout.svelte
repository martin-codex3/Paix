<script lang="ts">

	let { children } = $props();

</script>


<main>
	<nav>
		<div class="site__logo">
			<h1>logo</h1>
		</div>

		<div>
			<div>
				<ul>
					<li>
						<a href="/">
							<span>home</span>
						</a>
					</li>
				</ul>
			</div>
		</div>
	</nav>
	<section>
		{@render children()}
	</section>
</main>

