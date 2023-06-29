<template>
		<div class="wrapper">
			<div class="wrapper-inner">
				<div class="form-wrapper">
					<div class="form-title">
						<h2>Forgot Password</h2>
						<span>A password reset link will be sent to your email</span>
					</div>
					<div class="form-wrapper-inner has-login">
						<form action="" method="">
							<label for="email" class="form-label">Enter email address</label>
							<div class="form-input">
								<input type="email" class="form-control" id="email" placeholder="Email" />
							</div>

							<div class="submit-btn is-forgot">
								<button type="submit">RESET PASSWORD</button>
							</div>
						</form>
					</div>
					<div class="back-to-login">
            <router-link to="/login" class="">
							<span
								><svg
									xmlns="http://www.w3.org/2000/svg"
									width="1em"
									height="1em"
									preserveAspectRatio="xMidYMid meet"
									viewBox="0 0 16 16">
									<g transform="rotate(90 8 8) translate(0 16) scale(1 -1)">
										<path
											fill="currentColor"
											fill-rule="evenodd"
											d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z" />
									</g></svg
							></span>
							<span>Back to Log In</span>
            </router-link>
					</div>
				</div>
			</div>
		</div>
</template>

<style scoped>
@import "@/assets/static/css/styles/globalstyles.css";
@import "@/assets/static/css/auth-styles/auth.css";
</style>
