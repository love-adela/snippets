/* Strict mode */
/* Code reference:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode
 */

/* Invoking strict mode */
/* 1. Strict mode for scripts */
// Whole-script strict mode syntax
'use strict';
var v = "Hi! I'm a strict mode script!";
/* 2. Strict mode for functions */
function strict() {
  // function-level strict mode syntax
  'use strict';
  function nested() { return "And so am I"; }
  return "Hi! I'm a strict mode function! " + nested();
}
function notStrict() { return "I'm not strict."; }
/* 3. Strict mode for modules */
function strict() {
  // because this is a module, I'm strict by default
}
export default strict;

/* Changes in strict mode */
/* 1. Converting mistakes into errors */
"use strict";
                      // Assuming no global variable mistypeVariable exists
mistyedVariable = 17; // this line throws a ReferenceError due to the 
                      // misspelling of variable
// Strict mode makes assignments which would otherwise silently fail to throw an
// exception.
"use strict";
// Assignment to a non-writable global
var undefined = 5; // throws a TypeError
var Infinity = 5;  // throws a TypeError
// Assignment to a non-writable property
var obj1 = {};
Object.defineProperty(objs1, 'x', { value: 42, writable: false });
obj1.x = 9; // throws a TypeError
// Assignment to a getter-only property
var obj2 = { get x() { return 17; } };
obj2.x = 5; // throws a TypeError
// Assignement to a new property on a non-extensible object
var fixed = {};
Object.preventExtensions(fixed);
fixed.newProp = 'ohai'; // throws a TypeError
// Strict mode makes attempts to delete undeletable properties throw
// (where before the attempt would have no effect)
"use strict";
delete Object.prototype; // throws a TypeError.
// Strict mode requires that function parameter names be unique.
function sum(a, a, c) { // !!! syntax error
  'use strict';
  return a + a + c; // wrong if this code ran
}
// A strict mode in ECMAScript 5 forbids 0-prefixed octal literal or octal
// escape sequence.
var a = 0o10; // ES2015: Octal
// A leading zero syntax for the octals is rarely useful and can be mistakenly
// used.
'use strict';
var sum = 015 + // !!! syntax error
          197 +
          142;

var sumWithOctal = 0o10 + 8;
console.log(sumWithOctal); // 16;
// Strict mode in ECMAScript2015 forbids setting properties on primitive values.
(function() {
  'use strict';
  false.true = '';         // TypeError
  (14).sailing = 'home';   // TypeError
  'with'.you = 'far away'; // TypeError
})();
// In ECMAScript5 strict-mode code, duplicate property names were considered a
// SyntaxError.
'use strict';
var o = { p:1, p:2 }; // syntax error prior to ECMAScript2015
/* 2. Simplifying variable uses */
// Strict mode prohibits with.
'use strict';
var x = 17;
with (obj) { // !!! syntax error
  // If this weren't strict mode, would this be var x, or
  // would it instead be obj.x? It's impossible in general
  // to say without running the code, so the name can't be
  // optimized.
  x;
}
// `eval` of strict mode code does not introduce new variables into the
// surrounding scope.
var x = 17;
var evalX = eval("'use strict'; var x = 42; x");
console.assert(x === 17);
console.assert(evalX === 42);

// If the function `eval` is invoked by an expression of the form eval(...) in
// strict mode code, the code will be evaluated as strict mode code. The code
// may explicitly invoke strict mode, but it's unnecessary to do so.
function strict1(str) {
  'use strict';
  return eval(str); // str will be treated as strict mode code
}
function strict2(f, str) {
  'use strict';
  return f(str); // not eval(...): str is strict if and only
                 // if it invokes strict mode
}
function nonstrict(str) {
  return eval(str); // str is strict if and only
                    // if it invokes strict mode
}
strict1("'Strict mode code!'");
strict2("'use strict'; 'Strict mode code!'");
strict2(eval, "'Non-strict code.'");
strict2(eval, "'use strict'; 'Strict mode code!'");
nonstrict("'Non-strict code.'");
nonstrict("'use strict'; 'Strict mode code!'");
// Strict mode forbids deleting plain names. `delete name` in strict mode is a
// syntax error.
'use strict';

var x;
delete x; // !!! syntax error
eval('var y; delete y;'); // !!! syntax error
/* 3. Making eval and arguments simpler */
// `eval` and `arguments` can't be bound or assigned in language syntax.
'use strict';
eval = 17;
arguments++;
++eval;
var obj = { set p(arguments) { } };
var eval;
try { } catch (arguments) { }
function x(eval) { }
function arguments() { }
var y = function eval() { };
var f = new Function('arguments', "'use strict'; return 17;");
// Strict mode code doesn't alias properties of `arguments` objects created
// within it.

function f(a) {
  'use strict';
  a = 42;
  return [a, arguments[0]];
}
var pair = f(17);
console.assert(pair[0] === 42);
console.assert(pair[1] === 17);
// `arguments.callee` is no longer supported.
"use strict";
var f = function() { return arguments.callee; };
f(); // TypeError
/* 4. "Securing" JavaScript */
// The value passed as `this` to a function in strict mode is not forced into
// being an object (a.k.a. "boxed").
'use strict';
function fun() { return this; }
console.assert(fun() === undefined);
console.assert(fun.call(2) === 2);
console.assert(fun.apply(null) === null);
console.assert(fun.call(undefined) === undefined);
console.assert(fun.bind(true) () === true);
// In strict mode it's no longer possible to "walk(걷다)" the JavaScript stack
// via commonly implemented extensions to ECMAScript.
function restricted() {
  "use strict";
  restricted.caller; // throws a TypeError
  restricted.arguments; // throws a TypeError
}
function privilegedInvoker() {
  return restricted();
}
privilegedInvoker();
// arguments for strict mode functions no longer provide access to the
// corresponding function call's variables.
'use strict';
function fun(a, b) {
  'use strict';
  var v = 12;
  return arguments.caller; // throws a TypeError
}
fun(1, 2); // doesn't expose v (or a or b)

/* 5. Paving the way for future ECMAScript versions */
// In strict mode, a short list of identifiers become reserved keywords.
// These are `implements`, `interface`, `let`, `package`, `private`, `protected`,
// `public`, `static`, and `yield`.
function package(protected) { // !!!
  'use strict';
  var implements; // !!!

  interface: // !!!
  while (true) {
    break interface; // !!!
  }

  function private() { } // !!!
}
function fun(static) { 'use strict'; } // !!!
// Strict mode prohibits function statements that are not at the top level of
// script or function. In normal mode in brwosers, function statements are
// permitted "everywhere". This is not part of ES5. Note that function
// statements outside top level are permitted in ES2015.
'use strict';
if (true) {
  function f() { } // !!! syntax error
  f();
}
for (var i = 0; i < 5; i++) {
  function f2() { } // !!! syntax error
  f2();
}

function baz() { // kosher
  function eit() { } // also kosher
}
