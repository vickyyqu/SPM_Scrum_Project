const { Builder, By, until } = require("selenium-webdriver");
const assert = require("assert");

async function logoutTest() {
  driver = await new Builder().forBrowser("chrome").build();
  await driver.get("http://127.0.0.1:5173/");
  await driver.wait(until.titleIs("Skills-Based Role Portal"), 10000);

  const button_role = await driver.findElement(
    By.xpath('//button[contains(text(), "Staff")]')
  );
  await button_role.click();

  const inputField_staffID = await driver.findElement(
    By.xpath(`//input[@placeholder="Enter your staff ID"]`)
  );
  await inputField_staffID.sendKeys("140002");

  const inputField_password = await driver.findElement(
    By.xpath(`//input[@placeholder="Enter your password"]`)
  );
  await inputField_password.sendKeys("smu123");

  const button_login = await driver.findElement(
    By.xpath('//button[contains(text(), "Login")]')
  );
  await button_login.click();

  await driver.wait(until.elementLocated(By.className("sidebar")), 5000);

  const button_navbar = await driver.findElement(
    By.className("navbar-toggler")
  );
  await button_navbar.click();

  // Locate the navigation link element by its text (e.g., "About Us")
  const logOutLink = await driver.wait(
    until.elementLocated(By.linkText("Log Out")),
    10000
  );

  // Click on the navigation link
  logOutLink.click();

  // Define the expected elements on the target page
  const expectedElement = By.className("table-striped");

  // Wait for the element to be located and visible
  const element_logintable = await driver.wait(
    until.elementLocated(expectedElement),
    10000
  );
  await driver.wait(until.elementIsVisible(element_logintable), 10000);

  // Use assertions to check if the element is present and visible
  assert.ok(element_logintable, "Element should be present");

  await driver.quit();
}

logoutTest();
