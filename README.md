# rfremotewrapper

  ```powershell
  pip install build
  ```

Generate the wheel:

  ```powershell
  python -m build --wheel
  ```
 
 Add/replace keyword libraries in
 
   ```powershell
  robotframework-javaremote.whl/JavaRemote/lib/jrobotremoteserver.jar/
  ```

MWE (already included)

```java
import org.robotframework.javalib.annotation.ArgumentNames;
import org.robotframework.javalib.annotation.RobotKeyword;
import org.robotframework.javalib.annotation.RobotKeywords;

import javax.swing.JOptionPane;

@RobotKeywords
public class MyKeywords {
    @RobotKeyword("Say Hello")
    @ArgumentNames({"name"})
    public void sayHello(String name) {
        JOptionPane.showMessageDialog(null, "Hello " + name);
    }
}
```

Compile it with

```powershell
javac -cp jrobotremoteserver.jar MyKeywords.java
```

Install the library

  ```powershell
  pip install robotframework-javaremote.whl
  ```
