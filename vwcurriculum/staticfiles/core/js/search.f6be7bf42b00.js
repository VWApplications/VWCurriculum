function searchCertificate() {
  var input, ul;
  input = document.getElementById('searchCertificateInput');
  ul = document.getElementById("searchCertificateUL");
  search(input, ul)
}

function searchProject() {
  var input, ul;
  input = document.getElementById('searchProjectInput');
  ul = document.getElementById("searchProjectUL");
  search(input, ul)
}

function searchExperience() {
  var input, ul;
  input = document.getElementById('searchExperienceInput');
  ul = document.getElementById("searchExperienceUL");
  search(input, ul)
}

function search(input, ul) {
  var filter, li, span, i;
  filter = input.value.toUpperCase();
  li = ul.getElementsByTagName('li');
  for (i = 0; i < li.length; i++) {
    span = li[i].getElementsByTagName("span")[0];
    if (span.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
