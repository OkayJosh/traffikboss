<template>
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
					<div class="offcanvas-header">
						<button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
					</div>
					<div class="offcanvas-body">
						<div class="mobile-nav-links">
							<ul>
								<li>
                  <router-link to="/login" class="login">Log In</router-link>
								</li>
								<li>
                  <router-link to="/register" class="register">Register</router-link>
								</li>
							</ul>
						</div>
					</div>
				</div>
</template>
<script setup>
</script>