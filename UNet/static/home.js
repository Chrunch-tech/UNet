const brand_name = document.getElementById("brand-name");
const login_link = document.getElementById("login-link");
const register_link = document.getElementById("register-link");

brand_name.addEventListener("mouseover", () => {
  brand_name.id = "brand-name-hover-active";
});

brand_name.addEventListener("mouseout", () => {
  brand_name.id = "brand-name";
});

login_link.addEventListener("mouseover", () => {
  login_link.id = "login-link-hover";
});

login_link.addEventListener("mouseout", () => {
  login_link.id = "login-link";
});

register_link.addEventListener("mouseover", () => {
  register_link.id = "register-link-hover";
});

register_link.addEventListener("mouseout", () => {
  register_link.id = "register-link";
});

login_link.addEventListener("click", () => {
  login_link.id = "login-link-click";
});

register_link.addEventListener("click", () => {
  register_link.id = "register-link-click";
});
