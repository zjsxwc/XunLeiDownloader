<?php

$taskFile = __DIR__ . "/task.txt";
if ($_GET["type"]==="fetch_task") {
	$task = @file_get_contents($taskFile);
	if (!$task) {
		$task = "";
	}
	echo $task;

	file_put_contents($taskFile, "");
	exit;
}

if (isset($_POST["task"])) {
	$task = $_POST["task"];
	file_put_contents($taskFile, $task);
	echo "OK";
	exit;
}

echo 
<<<EOF
    <form method="post">
    	<textarea name="task"></textarea>
    	<button type="submit">Submit</button>
    </form>
EOF;



