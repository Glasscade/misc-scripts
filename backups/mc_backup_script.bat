@echo off
setlocal

:: folder paths
set SourceFolder=C:\Users\Local User\AppData\Roaming\.minecraft\saves\Survival
set GoogleDriveFolder=C:\Users\Local User\My Drive\_MC World Backups
set BackupFilename=MinecraftWorldBackup.zip
set SecondaryDriveFolder=D:\Backups\Minecraft World


:: Create a ZIP
powershell -command "Compress-Archive -Path '%SourceFolder%' -DestinationPath '%GoogleDriveFolder%\%BackupFilename%' -Force"

powershell -command "Compress-Archive -Path '%SourceFolder%' -DestinationPath '%SecondaryDriveFolder%\%BackupFilename%' -Force"

:: errorchecking
if %errorlevel% equ 0 (
    echo Backup completed successfully.
    powershell -command "& {Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Backup completed successfully', 'Backup Status')}"
) else (
    echo Backup failed.
    powershell -command "& {Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Backup failed', 'Backup Status')}"
)

endlocal
