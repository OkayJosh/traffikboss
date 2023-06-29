<template>
  <div class="wrapper">
			<div class="wrapper-inner">
				<div class="form-wrapper">
					<div class="form-title">
						<h2>Register</h2>
					</div>
					<div class="form-wrapper-inner">
						<form action="" method="" id="register">
							<div class="form-input">
								<input type="text" class="form-control" id="username" placeholder="Username" />
							</div>
							<div class="form-input">
								<input type="email" class="form-control" id="email" placeholder="Email" />
							</div>
							<div class="form-input">
								<input type="password" class="form-control" id="password" placeholder="Password" />
								<em class="bi bi-eye"></em>
							</div>
							<div class="form-input">
								<input type="password" class="form-control" id="confirmpass" placeholder="Confirm password" />
								<em class="bi bi-eye"></em>
							</div>
							<div class="submit-btn">
								<div class="agreement">
									<div class="form-check">
										<input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" />
										<label class="form-check-label" for="flexCheckDefault">
											I agree to have read the Terms of use and Privacy policy
										</label>
									</div>
								</div>
								<button type="submit">REGISTER</button>
							</div>
						</form>
					</div>
					<hr />
					<div class="other-method">
						<ul>
							<li><a href="#">Google</a></li>
							<li><a href="#">Facebook</a></li>
						</ul>
					</div>
				</div>
				<div class="form-footer">
					<div class="form-footer-inner">
            <span>Already have an account ? <router-link to="/login">Log in</router-link></span>
					</div>
				</div>
			</div>
		</div>
</template>