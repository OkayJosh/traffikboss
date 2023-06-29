<template>
		<div class="wrapper">
			<div class="wrapper-inner">
				<div class="form-wrapper">
					<div class="form-title">
						<h2>Log In</h2>
					</div>
					<div class="form-wrapper-inner has-login">
						<form action="" method="" id="login">
							<div class="form-input">
								<input type="email" class="form-control" id="email" placeholder="Email" />
							</div>
							<div class="form-input">
								<input type="password" class="form-control" id="password" placeholder="Password" />
								<em class="bi bi-eye"></em>
							</div>

							<div class="submit-btn">
                <div class="agreement">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" />
                        <label class="form-check-label" for="flexCheckDefault">Remember me</label>
                    </div>
                    <div class="forgot-password">
                        <label class="form-check-label" for="flexCheckDefault">
                          <router-link to="/forgot-password" class="register">Forgot Password</router-link>
                        </label>
                    </div>
                </div>
								<button type="submit">Login</button>
							</div>
						</form>
					</div>
					<hr />
					<div class="other-method">
						<ul>
							<li><a href="#">Linkedin</a></li>
							<li><a href="#">Facebook</a></li>
						</ul>
					</div>
				</div>
				<div class="form-footer has-login">
					<div class="form-footer-inner">
						<span>Don't have an account ?
              <router-link to="/register" class="register">Register</router-link></span>
					</div>
				</div>
			</div>
		</div>
</template>

<style scoped>
@import "../assets/static/css/auth-styles/auth.css";

.agreement {
    display: flex;
    justify-content: space-between;
}

.forgot-password {
    margin-left: auto;
}

</style>

<script>
</script>