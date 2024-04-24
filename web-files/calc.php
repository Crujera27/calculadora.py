<?php
/*
   ____      _            _           _
  / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _   _ __  _   _
 | |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` | | '_ \| | | |
 | |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |_| |_) | |_| |
  \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_(_) .__/ \__, |
                                                        |_|    |___/
   Copyright (c) 2024 Ángel Crujera (angel.c@galnod.com)
 
       GitHub: https://github.com/Crujera27
       Web: https://crujera.galnod.com
       Licencia del proyecto: MIT

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
 
*/

$valid_username = 'mysupersecretdefaultuser';
$valid_password = 'mysupersecretdefaultpassword';


if(!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    echo 'Authentication required.';
    exit;
}
if($_SERVER['PHP_AUTH_USER'] != $valid_username || $_SERVER['PHP_AUTH_PW'] != $valid_password) {
    header('HTTP/1.0 401 Unauthorized');
    echo 'Invalid username or password.';
    exit;
}
if(isset($_GET['operation'])) {
    $operation = $_GET['operation'];
    if(is_complex_operation($operation)) {
        http_response_code(400);
        echo "Error: Operación muy compleja.";
        exit;
    }
    $result = execute_operation($operation);

    echo $result;
} else {
    http_response_code(400);
    echo "Error: Operación no proporcionada";
    exit;
}

function is_complex_operation($operation) {
    $complex_chars = ['^', 'sqrt'];

    foreach($complex_chars as $char) {
        if(strpos($operation, $char) !== false) {
            return true;
        }
    }

    return false;
}

function execute_operation($operation) {
    $operation = str_replace('x', '*', $operation);

    while(preg_match('/\(([^\(\)]+)\)/', $operation, $matches) || preg_match('/\[([^\[\]]+)\]/', $operation, $matches)) {
        $sub_operation = $matches[0];
        $sub_result = calculate_expression($matches[1]);
        $operation = str_replace($sub_operation, $sub_result, $operation);
    }
    $result = calculate_expression($operation);

    return $result;
}

function calculate_expression($expression) {
    eval('$result = '.$expression.';');

    return $result;
}
?>
